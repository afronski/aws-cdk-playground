import cloudwatch = require('@aws-cdk/aws-cloudwatch');
import sqs = require('@aws-cdk/aws-sqs');
import { Construct, Duration } from '@aws-cdk/core';

// export interface DeadLetterQueueProps {
//     /*
//      * The amount of days messages will live in the dead letter queue
//      *
//      * Cannot exceed 14 days.
//      *
//      * @default 14
//      */
//     retentionDays?: number;
// }

export class DeadLetterQueue extends sqs.Queue {
  public readonly messagesInQueueAlarm: cloudwatch.IAlarm;

  constructor(scope: Construct, id: string/*, props: DeadLetterQueueProps = {}*/) {
    // if (props.retentionDays !== undefined && props.retentionDays > 14) {
    //   throw new Error('retentionDays may not exceed 14 days');
    // }

    super(scope, id, {
        // retentionPeriod: Duration.days(14)
        // retentionPeriod: Duration.days(props.retentionDays || 14)
    });

    this.messagesInQueueAlarm = new cloudwatch.Alarm(this, 'Alarm', {
      alarmDescription: 'There are messages in the Dead Letter Queue',
      evaluationPeriods: 1,
      threshold: 1,
      // period: Duration.minutes(1),
      metric: this.metricApproximateNumberOfMessagesVisible()
    });
  }
}
