%{!?upstream_version: %global upstream_version %{version}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order

%{?dlrn: %global tarsources proliantutils-%{upstream_version}}
%{!?dlrn: %global tarsources proliantutils}

Name:           python-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
Version:        XXX
Release:        XXX
License:        Apache-2.0
URL:            https://github.com/openstack/proliantutils

Source0:        https://opendev.org/x/proliantutils/archive/%{upstream_version}.tar.gz

BuildArch:      noarch

%description
Client Library for interfacing with various devices in HP Proliant Servers

%package -n     python3-proliantutils
Summary:        Client Library for interfacing with various devices in HP Proliant Servers

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  openstack-macros
BuildRequires:  git-core
%prep
%autosetup -v -p 1 -n %{tarsources} -S git

rm -rf *.egg-info


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# In RDO we are managint pyasn1 for pysnmp via dependency in pysnmp-lextudio. To avoid
# conflicts between packages, let's remove pyasn1* from automatic deps.
sed -i '/^pyasn1.* /d' requirements.txt

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%install
%pyproject_install

%description -n     python3-proliantutils
Client Library for interfacing with various devices in HP Proliant Servers

%files -n     python3-proliantutils
%license LICENSE
%doc README.rst
%{python3_sitelib}/proliantutils*
%exclude %{python3_sitelib}/proliantutils/*test*

%changelog
