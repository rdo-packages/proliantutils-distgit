# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://github.com/openstack/proliantutils

Source0:        https://tarballs.openstack.org/proliantutils/proliantutils-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
Client Library for interfacing with various devices in HP Proliant Servers

%package -n     python%{pyver}-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
%{?python_provide:%python_provide python%{pyver}-proliantutils}

BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  openstack-macros
Requires: python%{pyver}-six >= 1.9.0
Requires: python%{pyver}-oslo-concurrency >= 3.8.0
Requires: python%{pyver}-oslo-utils  >= 3.20.0
Requires: python%{pyver}-oslo-serialization >= 1.10.0
Requires: python%{pyver}-jsonschema
Requires: python%{pyver}-requests
Requires: python%{pyver}-sushy >= 3.1.0
Requires: python%{pyver}-pbr >= 2.0.0

# Handle python2 exception
%if %{pyver} == 2
Requires: pysnmp
Requires: python-retrying
%else
Requires: python%{pyver}-pysnmp
Requires: python%{pyver}-retrying
%endif

%prep
%autosetup -v -p 1 -n proliantutils-%{upstream_version}

rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%description -n     python%{pyver}-proliantutils
Client Library for interfacing with various devices in HP Proliant Servers

%files -n     python%{pyver}-proliantutils
%license LICENSE
%doc README.rst
%{pyver_sitelib}/proliantutils*
%exclude %{pyver_sitelib}/proliantutils/*test*

%changelog
