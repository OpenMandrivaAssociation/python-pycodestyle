Summary:	Python style guide checker
Name:		python-pycodestyle
Version:	2.11.1
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://github.com/PyCQA/pycodestyle
Source0:	https://github.com/PyCQA/pycodestyle/archive/%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)
BuildArch:	noarch

%description
pycodestyle is a tool to check your Python code against some of the style
conventions in PEP 8.

%files
%{_bindir}/pycodestyle
%{py_puresitedir}/pycodestyle*
#{py_puresitedir}/__pycache__/*

%prep
%autosetup -p1 -n pycodestyle-%{version}

%build
python setup.py build

%install
python setup.py install --root %{buildroot}
