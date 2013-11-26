Name:				voms-config-wlcg
Version:			1.0.0
Release:			1%{?dist}
Summary:			VOMS Environment for wlcg clients
Group:				Applications/Internet
License:			CC0
URL:				https://svnweb.cern.ch/trac/lcgutil/wiki
Source0:			http://grid-deployment.web.cern.ch/grid-deployment/dms/lcgutil/tar/%{name}/%{name}-%{version}.tar.gz
BuildRoot:			%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:		cmake
BuildArch:			noarch

Requires:			voms%{?_isa}

%description
%{name} provides a configured environment for the common 
Virtual Organization (VO) of The Worldwide LHC Computing Grid (WLCG)

%clean
rm -rf %{buildroot};


%prep
%setup -q

%build
%cmake .

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%files
%config(noreplace) %{_sysconfdir}/vomses
%config(noreplace) /etc/grid-security/vomsdir
%doc README

%changelog
* Thu Nov 07 2013 Adrien Devresse <adevress at cern.ch>  
 - Initial version of voms config wlcg

