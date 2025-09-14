subarch: arm64
chost: aarch64-unknown-linux-musl
target: stage1
version_stamp: musl-hardened-@Timestamp@
rel_type: 23.0-musl-hardened
profile: default/linux/arm64/23.0/musl/hardened
snapshot_treeish: d2e6802f8cc12a24b33884966985008b8492b3ab
source_subpath: default/stage3-arm64-musl-hardened-20250907T230408Z.tar.xz
interpreter: /usr/bin/qemu-aarch64
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: /var/tmp/catalyst/releng/releases/portage/stages-qemu
portage_prefix: releng
