[collect ./stage/main.spec]

[section steps]

chroot/run: [
#!/bin/bash
$[[steps/setup]]
USE="build" emerge --oneshot --nodeps $eopts portage || exit 1
export USE="$[portage/USE] bindist"
emerge $eopts --deep --newuse -u system || exit 1
if [ "$[emerge/packages/force?]" = "yes" ]
then
	emerge --deep --newuse -u $eopts $[emerge/packages/force:lax] || exit 2
fi
# now, zap the world file....
rm -f /var/lib/portage/world || exit 4
if [ "$[emerge/packages?]" = "yes" ]
then
	emerge --deep --newuse -u $eopts $[emerge/packages:lax] || exit 1
fi
emerge $eopts @preserved-rebuild || exit 3
# to handle lib upgrades, etc.
]
#make sure the parser detects stray data out here....
[section portage]

ROOT: /

