from understack_workflows.topology import pxe_interface_name
from understack_workflows.topology import switch_connections

NAUTOBOT_DATA = {
    "id": "a3a2983f-d906-4663-943c-c41ab73c9b62",
    "interfaces": [
        {
            "connected_interface": {
                "device": {
                    "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129"},
                    "name": "f20-2-1.iad3.rackspace.net",
                    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6"},
                    "rel_vlan_group_to_devices": {
                        "rel_vlan_group_to_devices": [
                            {
                                "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                                "name": "f20-2-1.iad3.rackspace.net",
                            },
                            {
                                "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                                "name": "f20-2-2.iad3.rackspace.net",
                            },
                        ]
                    },
                },
                "id": "f9a5cc87-d10a-4827-99e8-48961fd1d773",
                "name": "Ethernet1/5",
            },
            "description": "Integrated NIC 1 Port 1",
            "id": "ac2f1eae-188e-4fc6-9245-f9a6cf8b4ea8",
            "ip_addresses": [],
            "mac_address": "D4:04:E6:4F:8D:B4",
            "name": "NIC.Integrated.1-1",
            "status": {"id": "d4bcbafa-3033-433b-b21b-a20acf9d1324"},
            "type": "A_25GBASE_X_SFP28",
        },
        {
            "connected_interface": {
                "device": {
                    "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129"},
                    "name": "f20-2-2.iad3.rackspace.net",
                    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6"},
                    "rel_vlan_group_to_devices": {
                        "rel_vlan_group_to_devices": [
                            {
                                "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                                "name": "f20-2-1.iad3.rackspace.net",
                            },
                            {
                                "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                                "name": "f20-2-2.iad3.rackspace.net",
                            },
                        ]
                    },
                },
                "id": "2148cf50-f70e-42c9-9f68-8ce98d61498c",
                "name": "Ethernet1/5",
            },
            "description": "Integrated NIC 1 Port 2",
            "id": "39d98f09-3199-40e0-87dc-e5ed6dce78e5",
            "ip_addresses": [],
            "mac_address": "D4:04:E6:4F:8D:B5",
            "name": "NIC.Integrated.1-2",
            "status": {"id": "d4bcbafa-3033-433b-b21b-a20acf9d1324"},
            "type": "A_25GBASE_X_SFP28",
        },
        {
            "connected_interface": {
                "device": {
                    "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129"},
                    "name": "f20-2-2.iad3.rackspace.net",
                    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6"},
                    "rel_vlan_group_to_devices": {
                        "rel_vlan_group_to_devices": [
                            {
                                "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                                "name": "f20-2-1.iad3.rackspace.net",
                            },
                            {
                                "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                                "name": "f20-2-2.iad3.rackspace.net",
                            },
                        ]
                    },
                },
                "id": "f72bb830-3f3c-4aba-b7d5-9680ea4d358e",
                "name": "Ethernet1/6",
            },
            "description": "NIC in Slot 1 Port 1",
            "id": "7ac587c4-015b-4a0e-b579-91284cbd0406",
            "ip_addresses": [],
            "mac_address": "14:23:F3:F5:25:F0",
            "name": "NIC.Slot.1-1",
            "status": {"id": "d4bcbafa-3033-433b-b21b-a20acf9d1324"},
            "type": "A_25GBASE_X_SFP28",
        },
        {
            "connected_interface": {
                "device": {
                    "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129"},
                    "name": "f20-2-1.iad3.rackspace.net",
                    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6"},
                    "rel_vlan_group_to_devices": {
                        "rel_vlan_group_to_devices": [
                            {
                                "id": "275ef491-2b27-4d1b-bd45-330bd6b7e0cf",
                                "name": "f20-2-1.iad3.rackspace.net",
                            },
                            {
                                "id": "05f6715a-4dbe-4fd6-af20-1e73adb285c2",
                                "name": "f20-2-2.iad3.rackspace.net",
                            },
                        ]
                    },
                },
                "id": "c210be75-1038-4ba3-9923-60050e1c5362",
                "name": "Ethernet1/6",
            },
            "description": "NIC in Slot 1 Port 2",
            "id": "8c28941c-02cd-4aad-9e3f-93c39e08b58a",
            "ip_addresses": [],
            "mac_address": "14:23:F3:F5:25:F1",
            "name": "NIC.Slot.1-2",
            "status": {"id": "d4bcbafa-3033-433b-b21b-a20acf9d1324"},
            "type": "A_25GBASE_X_SFP28",
        },
        {
            "connected_interface": {
                "device": {
                    "id": "912d38b1-1194-444c-8e19-5f455e16082e",
                    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129"},
                    "name": "f20-2-1d.iad3.rackspace.net",
                    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6"},
                    "rel_vlan_group_to_devices": None,
                },
                "id": "4d010e0f-3135-4769-8bb0-71ba905edf01",
                "name": "GigabitEthernet1/0/3",
            },
            "description": "Dedicated iDRAC interface",
            "id": "60d880c7-8618-414e-b4b4-fb6ac448c992",
            "ip_addresses": [
                {
                    "host": "10.46.96.156",
                    "id": "312d73f7-5b19-4cb4-b098-05d913ccef2d",
                    "parent": {"prefix": "10.46.96.128/26"},
                }
            ],
            "mac_address": "A8:3C:A5:35:43:86",
            "name": "iDRAC",
            "status": {"id": "d4bcbafa-3033-433b-b21b-a20acf9d1324"},
            "type": "A_25GBASE_X_SFP28",
        },
    ],
    "location": {"id": "da47f07f-b66a-4f0c-b780-4be8498e6129", "name": "IAD3"},
    "name": "Dell-33GSW04",
    "rack": {"id": "1ccd4b4a-7ba3-4557-b1ad-1ba87aee96a6", "name": "F20-2"},
}


def test_pxe_interface_name():
    assert pxe_interface_name(NAUTOBOT_DATA) == "NIC.Slot.1-2"


def test_switch_connections():
    assert switch_connections(NAUTOBOT_DATA) == {
        "NIC.Integrated.1-1": "f20-2-1.iad3.rackspace.net",
        "NIC.Integrated.1-2": "f20-2-2.iad3.rackspace.net",
        "NIC.Slot.1-2": "f20-2-1.iad3.rackspace.net",
        "NIC.Slot.1-1": "f20-2-2.iad3.rackspace.net",
        "iDRAC": "f20-2-1d.iad3.rackspace.net",
    }
