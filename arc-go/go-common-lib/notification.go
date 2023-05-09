package common

type NotificationType string

const (
	RoleType    NotificationType = "Role"
	ServiceType NotificationType = "Service"
	TagsType    NotificationType = "Tags"
)

type Notification struct {
	HashKey   string           `json:"hashKey,omitempty"`
	RangeKey  string           `json:"rangeKey,omitempty"`
	Version   int              `json:"version"`
	UpdatedAt int64            `json:"updatedAt"`
	Type      NotificationType `json:"type"`
}

type NotificationSystem interface {
	CreateTopic(topic string) (string, error)
	PublishNotification(topic string, message *Notification) error
}
