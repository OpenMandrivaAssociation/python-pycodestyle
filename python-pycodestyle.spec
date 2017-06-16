# Created by pyp2rpm-3.2.1
%global pypi_name pycodestyle

%define py2_build CFLAGS="%{optflags}" %{_bindir}/python2 setup.py  build --executable="/usr/bin/python2 -s"
%define py3_build CFLAGS="%{optflags}" %{_bindir}/python3 setup.py  build --executable="/usr/bin/python3 -s"

Name:           python-%{pypi_name}
Group:          Development/Python
Version:        2.3.1
Release:        1
Summary:        Python style guide checker

License:        MIT
URL:            https://pycodestyle.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

BuildRequires:  python3-devel
BuildRequires:  python-setuptools

%description
pycodestyle (formerly called pep8) Python style guide checker pycodestyle is a
tool to check your Python code against some of the style conventions in PEP
8_... _PEP 8: note:: This package used to be called pep8 but was renamed to
pycodestyle to reduce confusion. Further discussion can be found in the issue
where Guido requested this change < or in the lightning talk at PyCon 2016 by
...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python-setuptools
%description -n python2-%{pypi_name}
pycodestyle (formerly called pep8) Python style guide checker pycodestyle is a
tool to check your Python code against some of the style conventions in PEP
8_... _PEP 8: note:: This package used to be called pep8 but was renamed to
pycodestyle to reduce confusion. Further discussion can be found in the issue
where Guido requested this change < or in the lightning talk at PyCon 2016 by
...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-setuptools
%description -n python3-%{pypi_name}
pycodestyle (formerly called pep8) Python style guide checker pycodestyle is a
tool to check your Python code against some of the style conventions in PEP
8_... _PEP 8: note:: This package used to be called pep8 but was renamed to
pycodestyle to reduce confusion. Further discussion can be found in the issue
where Guido requested this change < or in the lightning talk at PyCon 2016 by
...

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%{_bindir}/python3 setup.py  install -O1 --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/pycodestyle %{buildroot}/%{_bindir}/pycodestyle-%{python3_version}
ln -s %{_bindir}/pycodestyle-%{python3_version} %{buildroot}/%{_bindir}/pycodestyle-3

%{_bindir}/python2 setup.py  install -O1 --skip-build --root %{buildroot}
cp %{buildroot}/%{_bindir}/pycodestyle %{buildroot}/%{_bindir}/pycodestyle-%{python2_version}
ln -s %{_bindir}/pycodestyle-%{python2_version} %{buildroot}/%{_bindir}/pycodestyle-2

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/pycodestyle
%{_bindir}/pycodestyle-2
%{_bindir}/pycodestyle-%{python2_version}

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/pycodestyle-3
%{_bindir}/pycodestyle-%{python3_version}

%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
