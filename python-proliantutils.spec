%{!?upstream_version: %global upstream_version %{version}}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        2.1.11
Release:        1%{?dist}
License:        ASL 2.0
URL:            https://github.com/stackforge/proliantutils

Source0:        https://pypi.io/packages/source/p/proliantutils/proliantutils-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: pysnmp
Requires: python-six >= 1.9.0
Requires: python-oslo-concurrency
Requires: python-oslo-utils
Requires: python-jsonschema
Requires: python-requests

%prep
%autosetup -v -p 1 -n proliantutils-%{upstream_version}

rm -rf *.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt tools/{pip,test}-requires

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
* Fri Sep 23 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.11-1
- Update to 2.1.11

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.9-1
- Update to 2.1.9


