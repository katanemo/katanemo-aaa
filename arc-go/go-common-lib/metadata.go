package common

type Metadata struct {
	AttributeName  string `dynamodbav:"attributeName" json:"attributeName"`
	AttributeValue string `dynamodbav:"attributeValue" json:"attributeValue"`
	UpdatedAt      int64  `dynamodbav:"updatedAt" json:"updatedAt"`
	CreatedAt      int64  `dynamodbav:"createdAt" json:"createdAt"`
	Version        int    `dynamodbav:"version" json:"version"`
}
