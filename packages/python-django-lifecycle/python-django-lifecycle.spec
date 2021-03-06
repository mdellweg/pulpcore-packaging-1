# Created by pyp2rpm-3.3.3
%global pypi_name django-lifecycle

Name:           python-%{pypi_name}
Version:        0.7.7
Release:        1%{?dist}
Summary:        Declarative model lifecycle hooks

License:        MIT
URL:            https://github.com/rsinger86/django-lifecycle
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-django >= 2.0
Requires:       python3-urlman >= 1.2.0

%description -n python3-%{pypi_name}
%{summary}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/django_lifecycle
%{python3_sitelib}/django_lifecycle-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Aug 25 2020 Evgeni Golov - 0.7.7-1
- Initial package.
