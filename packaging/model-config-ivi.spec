Name:		model-config-ivi
Summary:	A Model configuration
Version:	0.0.1
Release:	0
Group:		Automotive/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}/etc/config
cp -f model-config.xml %{buildroot}/etc/config/model-config.xml

%files
%manifest model-config.manifest
%license LICENSE.APLv2
%config /etc/config/model-config.xml
