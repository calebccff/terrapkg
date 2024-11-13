%global commit_date 20241113
%global kernel_version 6.12

%global tree_commit 28955f4fa2823e39f1ecfb3a37a364563527afbc
%global tree_shortcommit %(c=%{tree_commit}; echo ${c:0:7})

%global debug_package %{nil}
%define __os_install_post %{nil}

Name: linux-linaro-qcom
Version: %{kernel_version}_git%{commit_date}
Release: 1%{?dist}
Summary: Linux kernel for Qualcomm Snapdragon SoCs

License: GPL-2.0
URL: https://github.com/aarch64-laptops/linux
#        https://gitlab.com/linux-kernel/linux-next/-/archive/next-20241113/linux-next-next-20241113.tar.gz
Source0: https://gitlab.com/linux-kernel/linux-next/-/archive/next-%{commit_date}/linux-next-next-%{commit_date}.tar.gz
Source1: distro.config
Source2: devices.config

BuildRequires: bash bc bison findutils flex git openssl-devel perl python3 zstd

%description
Linaro-maintained Linux kernel for Qualcomm Snapdragon laptops.

%prep
ls -la
echo _sourcedir = %{_sourcedir}
echo _specdir = %{_specdir}
echo _builddir = %{_builddir}
echo _buildroot = %{_buildroot}
echo _topdir = %{_topdir}
cp %{_sourcedir}/distro.config %{_sourcedir}/arch/arm64/configs/
cp %{_sourcedir}/devices.config %{_sourcedir}/arch/arm64/configs/
make KBUILD_BUILD_VERSION="%{release}-next-${commit_date}" defconfig distro.config devices.config


%build
make KBUILD_BUILD_VERSION="%{release}-next-${commit_date}" %{?_smp_mflags}


%install
install -Dm644 arch/arm64/boot/vmlinuz.efi %{buildroot}/boot/linux.efi

make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc


%changelog
%autochangelog