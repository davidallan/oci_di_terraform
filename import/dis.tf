resource "oci_dataintegration_workspace" "dis_workspace" {
    #depends_on = [oci_identity_group.DISManage]
    #Required
    compartment_id = var.compartment_ocid
    display_name = var.workspace_display_name

    #Optional
    #defined_tags = {"Operations.CostCenter"= "42"}
    #freeform_tags = {"Department"= "Finance"}
    is_private_network_enabled = var.workspace_is_private_network_enabled
    subnet_id = var.workspace_subnet_id
    vcn_id = var.workspace_vcn_id
}

