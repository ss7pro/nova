#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.virt.libvirt.volume import volume as libvirt_volume


class LibvirtGPFSVolumeDriver(libvirt_volume.LibvirtBaseVolumeDriver):
    """Class for volumes backed by gpfs volume."""
    def __init__(self, connection):
        super(LibvirtGPFSVolumeDriver,
              self).__init__(connection, is_block_dev=False)

    def get_config(self, connection_info, disk_info):
        """Returns xml for libvirt."""
        conf = super(LibvirtGPFSVolumeDriver,
                     self).get_config(connection_info, disk_info)
        conf.source_type = "file"
        conf.source_path = connection_info['data']['device_path']
        return conf
