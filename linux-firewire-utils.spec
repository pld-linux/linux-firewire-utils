Summary:	Linux FireWire utilities
Summary(pl.UTF-8):	Narzędzia FireWire dla Linuksa
Name:		linux-firewire-utils
Version:	0.5.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://www.kernel.org/pub/linux/utils/ieee1394/%{name}-%{version}.tar.xz
# Source0-md5:	65537c716735fff29b99360feb9bd8cd
URL:		https://git.kernel.org/pub/scm/utils/ieee1394/linux-firewire-utils.git/
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The linux-firewire-utils package contains Linux FireWire utilities:
- config-rom-pretty-printer for printing content of configuration ROM
- lsfirewire and lsfirewirephy for listing devices
- firewire-request and firewire-phy-command for querying and
  configuring devices

%description -l pl.UTF-8
Pakiet linux-firewire-utils zawiera linuksowe narzędzia do FireWire:
- config-rom-pretty-printer do wypisywania zawartości ROM-u
  konfiguracji
- lsfirewire i lsfirewirephy do wypisywania urządzeń
- firewire-request i firewire-phy-command do odpytywania i
  konfiguracji urządzeń

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst TODO
%attr(755,root,root) %{_bindir}/config-rom-pretty-printer
%attr(755,root,root) %{_bindir}/firewire-phy-command
%attr(755,root,root) %{_bindir}/firewire-request
%attr(755,root,root) %{_bindir}/lsfirewire
%attr(755,root,root) %{_bindir}/lsfirewirephy
%{_mandir}/man8/config-rom-pretty-printer.8*
%{_mandir}/man8/firewire-phy-command.8*
%{_mandir}/man8/firewire-request.8*
%{_mandir}/man8/lsfirewire.8*
%{_mandir}/man8/lsfirewirephy.8*
