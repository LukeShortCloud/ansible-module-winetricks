# Ansible Module Winetricks

The Winetricks module for Ansible is used to manage Windows libraries in Wine via the use of [Winericks](https://wiki.winehq.org/Winetricks).


## Installation

Installation is optional. The only requirement is that Wine is installed onto the managed system.

Copy over the library into the default directory for Ansible's library.

```
$ sudo cp -r -v ansible-module-winetricks/library/ /usr/share/ansible/
```

The "library" directory can be included in the top-level directory of a Playbook to be bundled with it. Note that this software is distributed under the strict GPLv3 license to ensure that it always stays free and open source.

Alternatively, a Playbook can be executed to use this Git repository as an additional module library path.

```
$ ansible-playbook --module-path=/path/to/ansible-module-winetricks site.yml
```


## Usage

Module arguments:

| Name | Required | Default | Description
| --- | --- | --- | --- |
| args | Yes | | The arguments to use with Winetricks. |
| binary | No | | Specify a different Winetricks binary to use. This is useful for when multiple versions of Winetricks are installed on a system. |


## Testing

A simple Playbook is provided to test that the `winetest` binary will return the version. It is recommended to set the verbosity to 3 with the `ansible-playbook` command to see all of the results from the module.

```
$ ansible-playbook -vvv test.yml
```


## License

GPLv3
