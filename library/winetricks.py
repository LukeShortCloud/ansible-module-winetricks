#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: Winetricks

short_description: Manage Wine with Winetricks

version_added: ""

description:
    - "A module to manage Windows libraries in Wine with Winetricks"

options:
    args:
        description:
            - The arguments to provide to the Winetricks command
        required: true
    winetricks_binary:
        description:
            - Specify a custom path to a different Winetricks binary.
        required: false

author:
    - Luke Short (ekutlails)
'''

EXAMPLES = '''
- name: Install the Visual Basic C++ Redistributable 2013
  wine:
    winetricks_binary: /usr/bin/winetricks-20170823
    args: vcrun2013
'''

RETURN = '''
rc:
    description: The return code from the command.
    type: int
stdout:
    description: The standard output from the command.
    type: str
stderr:
    description: The standard error from the command.
    type: str
'''

from ansible.module_utils.basic import AnsibleModule

winetricks_binary = None

def run_module():

    module = AnsibleModule(
        argument_spec=dict(
            args=dict(type='str', required=True),
            winetricks_binary=dict(type='str', required=False),
        ),
        supports_check_mode=False
    )

    global winetricks_binary

    # Find and set the Winetricks binary path if it was not provided by the "winetricks_binary" argument.
    if not winetricks_binary:
        winetricks_binary = module.get_bin_path('winetricks', required=True)
        module.params['winetricks_binary'] = winetricks_binary

    result = dict(
        changed=True
    )

    # Put together the full command that will be run on the managed sytem.
    cmd = [winetricks_binary, "--unattended", module.params['args']]
    result['cmd'] = cmd
    # Run the command.
    rc, stdout, stderr = module.run_command(cmd)

    # Save the module results.
    result['rc'] = rc
    result['stdout'] = stdout
    result['stderr'] = stderr

    if rc == 0:
        module.exit_json(**result)
    else:
        module.fail_json(msg="Unexpected return code %s" % str(rc), **result)

def main():
    run_module()

if __name__ == '__main__':
    main()
