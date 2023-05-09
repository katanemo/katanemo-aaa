package aws

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/service/sns"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib"
	katconfig "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/config"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
)

type snsNotificationSystem struct {
	snsClient                        *sns.Client
	settings                         *katconfig.Settings
	publishNotificationCounter       common.Counter
	publishNotificationFailedCounter common.Counter
	createTopicCounter               common.Counter
}

func NewSnsNotificationSystem(settings *katconfig.Settings, metricsStore common.MetricsStore) common.NotificationSystem {
	snsClient := CreateSnsClient(settings)
	return &snsNotificationSystem{
		snsClient:                        snsClient,
		settings:                         settings,
		publishNotificationCounter:       metricsStore.NewCounter("sns_publish_notification"),
		publishNotificationFailedCounter: metricsStore.NewCounter("sns_publish_notification_failed"),
		createTopicCounter:               metricsStore.NewCounter("sns_create_topic"),
	}
}

func (s *snsNotificationSystem) CreateTopic(topic string) (string, error) {
	topicName := fmt.Sprintf("%s-%s", topic, s.settings.Environment)
	katlogger.Logger().Infof("creating sns topic: %v", topicName)
	resp, err := s.snsClient.CreateTopic(context.TODO(), &sns.CreateTopicInput{
		Name: &topicName,
	})
	if err != nil {
		return "", err
	}
	katlogger.Logger().Infof("created sns topic: %v", *resp.TopicArn)
	s.createTopicCounter.Inc()
	return *resp.TopicArn, nil
}

func (s *snsNotificationSystem) PublishNotification(topic string, message *common.Notification) error {
	s.publishNotificationCounter.Inc()
	jsonMessage, err := json.Marshal(message)
	if err != nil {
		s.publishNotificationFailedCounter.Inc()
		return err
	}

	topicArn := fmt.Sprintf("arn:aws:sns:%v:%v:%v-%v", s.settings.AwsRegion, s.settings.AwsAccountId, topic, s.settings.Environment)
	katlogger.Logger().Infof("writing message to sns topic: %v", topicArn)
	_, err = s.snsClient.Publish(context.TODO(), &sns.PublishInput{
		Message:  aws.String(string(jsonMessage)),
		TopicArn: &topicArn,
	})
	if err != nil {
		s.publishNotificationFailedCounter.Inc()
		katlogger.Logger().Errorf("writing message to sns failed: %v", err)
	}
	return err
}
