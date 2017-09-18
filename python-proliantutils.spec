%{!?upstream_version: %global upstream_version %{version}}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://github.com/openstack/proliantutils

Source0:        https://tarballs.openstack.org/proliantutils/proliantutils-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  openstack-macros
Requires: pysnmp
Requires: python-six >= 1.9.0
Requires: python-oslo-concurrency >= 3.8.0
Requires: python-oslo-utils  >= 3.20.0
Requires: python-oslo-serialization >= 1.10.0
Requires: python-jsonschema
Requires: python-requests
Requires: python-sushy >= 1.0.0
Requires: python-pbr >= 2.0.0
Requires: python-retrying

%prep
%autosetup -v -p 1 -n proliantutils-%{upstream_version}

rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
%py_req_cleanup

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%description
Client Library for interfacing with various devices in HP Proliant Servers

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/proliantutils*
%exclude %{python2_sitelib}/proliantutils/*test*

%changelog
