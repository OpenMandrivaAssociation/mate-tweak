Summary:	MATE desktop tweak tool
Name:		mate-tweak
Version:	22.10.0
Release:	1
License:	GPL-2.0-or-later
Group:		Graphical desktop/Other
URL:		https://github.com/ubuntu-mate/mate-tweak
Source:		https://github.com/ubuntu-mate/mate-tweak/archive/%{version}/%{name}-%{version}.tar.gz
# (OpenSUSE)
Patch0:		mate-tweak-use-matemenu.patch

BuildRequires:	dconf
BuildRequires:	fdupes
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(configobj)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(setproctitle)
BuildRequires:	python%{pyver}dist(setuptools)

Requires:	dconf
Requires:	mate-panel
Requires:	polkit
Requires:	python%{pyver}dist(configobj)
Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(python-distutils-extra)
Requires:	python%{pyver}dist(psutil)
Requires:	python%{pyver}dist(setproctitle)

Recommends:	mate-applet-indicator

BuildArch:	noarch

%description
Configures some aspects of the MATE desktop not exposed via the
MATE Control Centre applets.

Settings that can be handled via MATE Tweak:
 * Show/hide standard desktop icons.
 * Panel fine-tuning (icon visibility, in menus and on buttons,
   icon size, button labelling, contex menus, etc.).
 * Window manager fine-tuning.

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/marco-*
%{_prefix}/lib/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/marco-*.desktop
%{_datadir}/polkit-1/actions/org.mate.mate-tweak.policy
%{py_puresitedir}/mate_tweak-*.*-info
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/marco*.1*

#-----------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

# Give gi-find-deps.sh a bait.
#ln -s %{_bindir}/%{name} %{buildroot}%{_prefix}/lib/%{name}/%{name}.py

# remove unwanted
rm -f %{buildroot}%{python_sitelib}/setup.py

# locales
%find_lang %{name} --with-gnome --all-name

