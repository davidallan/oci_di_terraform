#!/usr/bin/env python3

# Copyright © 2023, Oracle and/or its affiliates. 
# The Universal Permissive License (UPL), Version 1.0 as shown at https://oss.oracle.com/licenses/upl.

import oci
import json
import requests
import sys
from oci.signer import Signer
from oci.data_integration.models import CreateImportRequestDetails
from oci.data_integration.models import ImportConflictResolution


###########################################################################################################################
# Start here
###########################################################################################################################

#config = oci.config.from_file('~/.oci/config')
# For raw-requests, get the signer auth
#auth = Signer(
#    tenancy=config['tenancy'],
#    user=config['user'],
#    fingerprint=config['fingerprint'],
#    private_key_file_location=config['key_file']
#)
#signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
#data_integration_client = oci.data_integration.DataIntegrationClient(config)

# Use Instance Principal in CloudShell
delegation_token = open('/etc/oci/delegation_token', 'r').read()
signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
   delegation_token=delegation_token
)

data_integration_client = oci.data_integration.DataIntegrationClient(config={'region': 'us-ashburn-1'}, signer=signer)

print(data_integration_client)
print(sys.argv)
workspaceID = sys.argv [1]
bucket_name = sys.argv [2]
file_name = sys.argv [3]
object_storage_tenancy_id = sys.argv [4]
object_storage_region = sys.argv [5]

cird = CreateImportRequestDetails(bucket_name=bucket_name, file_name=file_name,object_storage_tenancy_id=object_storage_tenancy_id,object_storage_region=object_storage_region,import_conflict_resolution=ImportConflictResolution(import_conflict_resolution_type="RETAIN"))
data_integration_client.create_import_request(workspaceID,cird);
