%global distributor_name openEuler
%global distributor_version %{openEuler}
%global url_ver %%(echo %{version}|cut -d. -f1,2)

Name:           gnome-boxes
Version:        3.38.2
Release:        1
Summary:        An application of the GNOME Desktop Environment
License:        LGPLv2+
URL:            https://wiki.gnome.org/Apps/Boxes
Source0:        http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:  gettext >= 0.19.8 meson itstool vala >= 0.36.0 yelp-tools
BuildRequires:  pkgconfig(clutter-gtk-1.0) pkgconfig(freerdp2) pkgconfig(glib-2.0) >= 2.52
BuildRequires:  pkgconfig(gobject-introspection-1.0) pkgconfig(govirt-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.20 pkgconfig(gtk-vnc-2.0) pkgconfig(libarchive)
BuildRequires:  pkgconfig(json-glib-1.0) pkgconfig(libsecret-1) pkgconfig(libvirt-gobject-1.0)
BuildRequires:  pkgconfig(libvirt-gconfig-1.0) pkgconfig(libxml-2.0) pkgconfig(gudev-1.0) libosinfo-vala
BuildRequires:  pkgconfig(libosinfo-1.0) >= 1.4.0 pkgconfig(libsoup-2.4) >= 2.44 pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(tracker-sparql-3.0) pkgconfig(webkit2gtk-4.0) spice-gtk3-vala libosinfo-vala
BuildRequires:  desktop-file-utils pkgconfig(libusb-1.0) pkgconfig(gtksourceview-4) spice-gtk spice-gtk-devel
Requires:       libvirt-daemon-kvm libvirt-daemon-config-network mtools genisoimage adwaita-icon-theme

%description
An application of the GNOME Desktop Environment,used to access remote or virtual systems.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson -D distributor_name=%{distributor_name} -D distributor_version=%{distributor_version} \
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Boxes.desktop

%files -f %{name}.lang
%exclude %{_includedir}/gnome-boxes/
%exclude %{_libdir}/gnome-boxes/{girepository-1.0,pkgconfig}
%exclude %{_datadir}/gnome-boxes/{gir-1.0,vapi}
%doc AUTHORS README.md NEWS COPYING
%{_bindir}/gnome-boxes
%{_libdir}/gnome-boxes
%{_libexecdir}/gnome-boxes-search-provider
%{_datadir}/applications/org.gnome.Boxes.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%{_datadir}/gnome-boxes/
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Boxes.SearchProvider.ini
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Boxes.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Boxes-symbolic.svg
%{_datadir}/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Boxes.service
%{_datadir}/metainfo/org.gnome.Boxes.appdata.xml

%changelog
* Tue Jun 22 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 3.38.2-1
- Upgrade to 3.38.2
- Delete two patches whoes content existed in this version 3.38.2

* Mon Apr 27 2020 wangyue<wangyue92@huawei.com> - 3.30.3-5
- Package init and fix build error
