Name:				voms-config
Version:			1.0.1
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


# Global Meta-package
%package all
Summary:			VOMS configuration for all VOs
Group:				Applications/Internet
Requires:			%{name}-vo-wlcg = %{version}-%{release}
Requires:			%{name}-vo-geant4 = %{version}-%{release}
Requires:			%{name}-vo-unosat = %{version}-%{release}
Requires:			%{name}-vo-ops = %{version}-%{release} 
Requires:			%{name}-vo-other = %{version}-%{release} 

%description all
VOMS configuration files for all the registered VOs




# WLCG Meta-package
%package wlcg
Summary:			VOMS configuration for all WLCG VOs
Group:				Applications/Internet
Requires:			%{name}-vo-atlas = %{version}-%{release}
Requires:			%{name}-vo-cms = %{version}-%{release} 
Requires:			%{name}-vo-lhcb = %{version}-%{release} 
Requires:			%{name}-vo-alice = %{version}-%{release} 
Requires:			%{name}-vo-dteam = %{version}-%{release}
Requires:			%{name}-vo-sixt = %{version}-%{release}

%description wlcg
VOMS configuration files for the the World LHC Computing Grid

# ATLAS VO
%package vo-atlas
Summary:			VOMS configuration files for atlas
Group:				Applications/Internet

%description vo-atlas
VOMS configuration files for the VO atlas

# CMS VO
%package vo-cms
Summary:			VOMS configuration files for cms
Group:				Applications/Internet
 
%description vo-cms
VOMS configuration files for the VO cms

# LHCB VO
%package vo-lhcb
Summary:			VOMS configuration files for lhcb
Group:				Applications/Internet
 
%description vo-lhcb
VOMS configuration files for the VO lhcb

# ALICE
%package vo-alice
Summary:				VOMS configuration files for alice
Group:					Applications/Internet
 
%description vo-alice
VOMS configuration files for the VO alice

#DTEAM
%package vo-dteam
Summary:				VOMS configuration files for dteam
Group:					Applications/Internet
 
%description vo-dteam
VOMS configuration files for the VO dteam

%package vo-sixt
Summary:				VOMS configuration files for sixt
Group:					Applications/Internet
 
%description vo-sixt
VOMS configuration files for the VO sixt


# OPS VO
%package vo-ops
Summary:				VOMS configuration files for ops
Group:					Applications/Internet
 
%description vo-ops
VOMS configuration files for the VO ops

# GEANT VO
%package vo-geant4
Summary:				VOMS configuration files for geant4
Group:					Applications/Internet
 
%description vo-geant4
VOMS configuration files for the VO geant4

# UNOSAT VO
%package vo-unosat
Summary:				VOMS configuration files for unosat
Group:				Applications/Internet
 
%description vo-unosat
VOMS configuration files for the VO unosat

# Other remaining VO
%package vo-other
Summary:				VOMS configuration files for other
Group:				Applications/Internet
 
%description vo-other
VOMS configuration files for the VO other



%clean
rm -rf %{buildroot};

%prep
%setup -q

%build
%cmake .

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%file wlcg
%doc README

%files vo-atlas
%config(noreplace) %{_sysconfdir}/vomses/atlas*
%config(noreplace) /etc/grid-security/vomsdir/atlas*

%files vo-cms
%config(noreplace) %{_sysconfdir}/vomses/cms*
%config(noreplace) /etc/grid-security/vomsdir/cms*

%files vo-lhcb
%config(noreplace) %{_sysconfdir}/vomses/lhcb*
%config(noreplace) /etc/grid-security/vomsdir/lhcb*

%files vo-alice
%config(noreplace) %{_sysconfdir}/vomses/alice*
%config(noreplace) /etc/grid-security/vomsdir/alice*

%files vo-dteam
%config(noreplace) %{_sysconfdir}/vomses/dteam*
%config(noreplace) /etc/grid-security/vomsdir/dteam*

%files vo-sixt
%config(noreplace) %{_sysconfdir}/vomses/vo.sixt*
%config(noreplace) /etc/grid-security/vomsdir/vo.sixt*

%files vo-ops
%config(noreplace) %{_sysconfdir}/vomses/ops*
%config(noreplace) /etc/grid-security/vomsdir/ops*

%files vo-geant4
%config(noreplace) %{_sysconfdir}/vomses/geant4*
%config(noreplace) /etc/grid-security/vomsdir/geant4*

%files vo-unosat
%config(noreplace) %{_sysconfdir}/vomses/unosat*
%config(noreplace) /etc/grid-security/vomsdir/unosat*

%files vo-other
%config(noreplace) %{_sysconfdir}/vomses/ilc*
%config(noreplace) /etc/grid-security/vomsdir/ilc*
%config(noreplace) %{_sysconfdir}/vomses/na48*
%config(noreplace) /etc/grid-security/vomsdir/na48*
%config(noreplace) %{_sysconfdir}/vomses/*egee*
%config(noreplace) /etc/grid-security/vomsdir/*egee*
%config(noreplace) %{_sysconfdir}/vomses/*aleph*
%config(noreplace) /etc/grid-security/vomsdir/*aleph*
%config(noreplace) %{_sysconfdir}/vomses/*delphi*
%config(noreplace) /etc/grid-security/vomsdir/*delphi*
%config(noreplace) %{_sysconfdir}/vomses/*opal*
%config(noreplace) /etc/grid-security/vomsdir/*opal*
%config(noreplace) %{_sysconfdir}/vomses/*l3*
%config(noreplace) /etc/grid-security/vomsdir/*l3*

%changelog
* Fri Sep 26 2014 Adrien Devresse <adevress at cern.ch> - 1.0.1-1
 - Update for SHA2 Update

* Thu Nov 07 2013 Adrien Devresse <adevress at cern.ch> - 1.0.0
 - Initial version of voms config wlcg

