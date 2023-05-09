package paths

import "testing"

func TestFLAC_match(t *testing.T) {
	type args struct {
		rolePath string
		resource string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "resource fields absent in policy",
			args: args{
				rolePath: "PUT:path:[nodeGroup.Size.Max, metadata, nodeGroup.name]",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": {
										"Max": 100,
										"Min": 10,
										"Average": 40
									}
								},
								"nodeGroupData": {
									"name": "node group 1",
									"Size": {
										"Max": 100,
										"Min": 10,
										"Average": 40
									}
								},
								"nodeGroup.name": "node group 2"
							}`,
			},
			want: false,
		},
		{
			name: "resource fields present in policy",
			args: args{
				rolePath: "PUT:path:[nodeGroup.Size.Max, metadata, nodeGroup.name]",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": {
										"Max": 100
									}
								},
								"nodeGroup.name": "node group 2"
							}`,
			},
			want: true,
		},
		{
			name: "policy with star",
			args: args{
				rolePath: "PUT:path:[nodeGroup*, metadata]",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": {
										"Max": 100
									}
								},
								"nodeGroup.name": "node group 2"
							}`,
			},
			want: true,
		},
		{
			name: "policy with star and dot",
			args: args{
				rolePath: "PUT:path:[nodeGroup.*, metadata]",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": {
										"Max": 100
									}
								},
								"nodeGroup.name": "node group 2"
							}
				`,
			},
			want: true,
		},
		{
			name: "missing policy with star",
			args: args{
				rolePath: "PUT:path:[nodeGroup.name*, metadata]",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": {
										"Max": 100
									}
								},
								"nodeGroup.name": "node group 2"
							}`,
			},
			want: false,
		},
		{
			// If there is no FLAC policy then it should be a match (if other conditions are matched.)
			name: "missing FLAC policy with resource",
			args: args{
				rolePath: "PUT:path",
				resource: `{
								"metadata": "metadata value",
								"nodeGroup": {
									"name": "node group 1",
									"Size": "Max": 100
								},
								"nodeGroup.name": "node group 2"
							}`,
			},
			want: true,
		},
		{
			name: "array type",
			args: args{
				rolePath: "PUT:path:nodeGroups.MaxSize",
				resource: `{
								"nodeGroups": [
									{
									"MaxSize": 100
									},
									{
										"MaxSize": 50
									}
								]
							}`,
			},
			want: true,
		},
		{
			name: "array type not matching policy",
			args: args{
				rolePath: "PUT:path:nodeGroups.Size",
				resource: `{
								"nodeGroups": [
									{
										"MaxSize": 100,
										"Name": "abc"
									},
									{
										"MaxSize": 50
									}
								]
							}`,
			},
			want: false,
		},
		{
			name: "array type matching policies",
			args: args{
				rolePath: "PUT:path:[nodeGroups.MaxSize,nodeGroups.Name]",
				resource: `{
								"nodeGroups": [
									{
										"Name": "abc",
										"MaxSize": 100
									}
								]
							}`,
			},
			want: true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FLACMatch(tt.args.rolePath, &tt.args.resource); got != tt.want {
				t.Errorf("FLAC_match() = %v, want %v", got, tt.want)
			}
		})
	}
}
