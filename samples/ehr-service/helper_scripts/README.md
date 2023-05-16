# Helper scripts to test EHR SaaS Service

Helper scripts to test and validate EHR service follow these steps,

1. navigate to samples/ehr-service/helper_scripts
    ```
    $ cd samples/ehr-service/helper_scripts
    ```
2. Signup EHR admin with katanemo
    > Use valid email address. Upon successful this script will place various account related details in `.ehr_admin_details`
    ```
    $ ehr_admin_signup.sh <ehr_admin_email>
    ```
3. Add EHR's openapi spec to katanemo,
    > Upon successful run copies service id in `.ehr_service_details`
    ```
    $ sh ehr_service_init.sh ../ehr.yaml
    ```
4. Subscribe to EHR service
    > Upon successful run copies subscriber related details like accountId and emails to `.subscriber_details`
    ```
    $ sh ehr_signup_subscriber.sh <subscriber_admin_email> <subscriber_doctor_email> <receptionist_email>
    ```

## Validation

Once you have successful ran `ehr_admin_signup.sh`, `ehr_service_init.sh` and `ehr_signup_subscriber.sh` you can go ahead and run `sh deploy.sh` with admin email from #1 and service Id from #2 from parent folder.

After deploy.sh is complete you can run validate.sh to run through various test cases.

```
$ sh validate.sh
```
