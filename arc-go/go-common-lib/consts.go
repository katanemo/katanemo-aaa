package common

const CreateByTag = "katanemo:createdBy"
const AssumeRoleGetTag = "katanemo:http:assumeRole:GET"
const TokenClaimAccountId = "accountId"
const TokenClaimServiceId = "aud"
const TokenClaimSubject = "sub"
const KatanemoServiceName = "Katanemo"
const KatanemoDefaultServiceId = "KatanemoDefaultServiceId"

const AuditLogsS3BucketPrefix = "katanemo-audit-logs-"
const AuditLogsEntryVersion = "1.0"

const SynthTrafficEmailPrefix = "synth-traffic"

type Environment string

const (
	EnvironmentDev     Environment = "dev"
	EnvironmentStaging Environment = "staging"
	EnvironmentProd    Environment = "prod"
)

const OpenApiSpecFileParamName = "apiSpecFile"

const AdminRoleDefaultPolicyContent = `{"version":1,"type":"default","policy":[{"allow":["*"]}]}`
const UserRoleDefaultPolicyContent = `{"version":1,"type":"default","policy":[{"allow":[]}]}`
