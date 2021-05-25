'use strict';

const AWS = require('aws-sdk');
var parse = AWS.DynamoDB.Converter.output;
const firehose = new AWS.Firehose({ region: 'us-east-1' });

exports.handler = (event, context, callback) => {

    var fireHoseInput = [];
    
    event.Records.forEach((record) => {

        console.log(record);
        
        if ((record.eventName == "INSERT")||(record.eventName == "MODIFY")) {
            fireHoseInput.push({ Data: JSON.stringify(parse({ "M": record.dynamodb.NewImage })) });
        }
    });

    var params = {
        DeliveryStreamName: 'streamtos3',
        Records: fireHoseInput
    };
    if(fireHoseInput.length != 0)
    {
    firehose.putRecordBatch(params, function (err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else console.log(data);           // successful response
    });
    }
    else
        {
            console.log("No data to transmit");
        }
    callback(null, `Successfully processed records.`);
};