%global vendor %{?_vendor:%{_vendor}}%{!?_vendor:openEuler}
%global distributor_name %{vendor}
%global distributor_version %{%{vendor}}
%global major_version %%(echo %%{tarball_version} | cut -d. -f1)

%global __provides_exclude_from ^%{_libdir}/gnome-boxes/
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/gnome-boxes/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))

Name:		gnome-boxes
Version:	42.1
Release:	2
Summary:        An application of the GNOME Desktop Environment
License:        LGPLv2+
URL:            https://wiki.gnome.org/Apps/Boxes
Source0:	https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
Patch1:         0002-disable-domain-conf-video-model-qxl-because-qemu-not-open-this-support.patch
Patch2:         0003-disable-domain-conf-smartcard-because-qemu-not-open-this-support-now.patch
Patch3:         0004-disable-domain-conf-spice-graphics-because-qemu-not-open-this-support-now-and-add-vnc-instead.patch
Patch4:         0005-disable-domain-conf-USB-redirection--because-qemu-this-version-unsupport-now.patch

BuildRequires:  gettext >= 0.19.8 meson itstool vala >= 0.36.0 yelp-tools
BuildRequires:  pkgconfig(clutter-gtk-1.0) pkgconfig(freerdp2) pkgconfig(glib-2.0) >= 2.52
BuildRequires:  pkgconfig(gobject-introspection-1.0) pkgconfig(govirt-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20 pkgconfig(gtk-vnc-2.0) pkgconfig(libarchive)
BuildRequires:  pkgconfig(json-glib-1.0) pkgconfig(libsecret-1) pkgconfig(libvirt-gobject-1.0)
BuildRequires:  pkgconfig(libvirt-gconfig-1.0) pkgconfig(libxml-2.0) pkgconfig(gudev-1.0) libosinfo-vala
BuildRequires:  pkgconfig(libosinfo-1.0) >= 1.4.0 pkgconfig(libsoup-2.4) >= 2.44 pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(tracker-sparql-3.0) pkgconfig(webkit2gtk-4.0) spice-gtk3-vala libosinfo-vala
BuildRequires:  desktop-file-utils pkgconfig(libusb-1.0) pkgconfig(gtksourceview-4) spice-gtk spice-gtk-devel chrpath
BuildRequires:	pkgconfig(gvncpulse-1.0) pkgconfig(libhandy-1)

Requires:       libvirt-daemon-kvm libvirt-daemon-config-network mtools genisoimage adwaita-icon-theme

%description
An application of the GNOME Desktop Environment,used to access remote or virtual systems.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson -D distributor_name=%{distributor_name} -D distributor_version=%{distributor_version}
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

chrpath -d %{buildroot}%{_bindir}/gnome-boxes
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/gnome-boxes" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

rm -rf %{buildroot}%{_includedir}/gnome-boxes/
rm -rf %{buildroot}%{_libdir}/gnome-boxes/girepository-1.0/
rm -rf %{buildroot}%{_libdir}/gnome-boxes/pkgconfig/
rm -rf %{buildroot}%{_datadir}/gnome-boxes/gir-1.0/
rm -rf %{buildroot}%{_datadir}/gnome-boxes/vapi/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Boxes.desktop

%files -f %{name}.lang
%license COPYING copyright
%doc README.md NEWS
%{_bindir}/gnome-boxes
%{_libdir}/gnome-boxes
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/gnome-boxes/
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_datadir}/icons/hicolor/*/apps/org.gnome.Boxes.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/metainfo/org.gnome.Boxes.appdata.xml
%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

%changelog
* Fri Nov 18 2022 yaoxin <yaoxin30@h-partners.com> - 42.1-2
- Replace openEuler with vendor

* Mon Oct 31 2022 yaoxin <yaoxin30@h-partners.com> - 42.1-1
- Update to 42.1

* Tue Mar 15 2022 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.2-4
- Add four patches to make gome-boxes avoid setting qemu unsupported modules
  add vnc instead of spice

* Mon Oct 11 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.2-3
- Add 0001-make-gnome-boxes-correctly-select-virtualization-cpu-mode.patch

* Fri Sep 10 2021 lingsheng <lingsheng@huawei.com> - 3.38.2-2
- Delete rpath setting

* Tue Jun 22 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.2-1
- Upgrade to 3.38.2
- Delete two patches whoes content existed in this version 3.38.2

* Mon Apr 27 2020 wangyue<wangyue92@huawei.com> - 3.30.3-5
- Package init and fix build error
