%{!?upstream_version: %global upstream_version %{version}}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        2.1.7
Release:        2%{?dist}
License:        ASL 2.0
URL:            https://github.com/stackforge/proliantutils

Source0:        https://pypi.python.org/packages/source/p/proliantutils/proliantutils-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  python2-devel
BuildRequires:  python-pbr
Requires: python-six
Requires: python2-oslo-concurrency
Requires: python2-oslo-utils
Requires: python-jsonschema

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
* Wed Sep 14 2016 Alejandro Andreu <alejandroandreu@openmailbox.org> 2.1.7-2
- Fix dependency naming for python-oslo-* packages

* Thu Mar 24 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.7-1
- Update to 2.1.7


