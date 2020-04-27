%{!?upstream_version: %global upstream_version %{version}}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        2.9.4
Release:        1%{?dist}
License:        ASL 2.0
URL:            https://github.com/openstack/proliantutils

Source0:        https://tarballs.openstack.org/proliantutils/proliantutils-%{upstream_version}.tar.gz

BuildArch:      noarch

%description
Client Library for interfacing with various devices in HP Proliant Servers

%package -n     python3-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
%{?python_provide:%python_provide python3-proliantutils}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  openstack-macros
Requires: python3-six >= 1.9.0
Requires: python3-oslo-concurrency >= 3.8.0
Requires: python3-oslo-utils  >= 3.20.0
Requires: python3-oslo-serialization >= 1.10.0
Requires: python3-jsonschema
Requires: python3-requests
Requires: python3-sushy >= 3.1.0
Requires: python3-pbr >= 2.0.0

Requires: python3-pysnmp
Requires: python3-retrying

%prep
%autosetup -v -p 1 -n proliantutils-%{upstream_version}

rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%description -n     python3-proliantutils
Client Library for interfacing with various devices in HP Proliant Servers

%files -n     python3-proliantutils
%license LICENSE
%doc README.rst
%{python3_sitelib}/proliantutils*
%exclude %{python3_sitelib}/proliantutils/*test*

%changelog
* Mon Apr 27 2020 RDO <dev@lists.rdoproject.org> 2.9.4-1
- Update to 2.9.4

