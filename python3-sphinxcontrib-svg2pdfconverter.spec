Summary:	Sphinx SVG to PDF converter extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa konwertujące SVG do PDF
Name:		python3-sphinxcontrib-svg2pdfconverter
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-svg2pdfconverter/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-svg2pdfconverter/sphinxcontrib_svg2pdfconverter-%{version}.tar.gz
# Source0-md5:	78da22aca351032a3866436892d97568
URL:		https://pypi.org/project/sphinxcontrib-svg2pdfconverter/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:61.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension converts SVG images to PDF in case the builder does not
support SVG images natively (e.g. LaTeX).

%description -l pl.UTF-8
To rozszerzenie konwertuje obrazy SVG do PDF w przypadkach, kiedy
builder sam nie obsługuje obrazów SVG (np. LaTeX).

%package apidocs
Summary:	API documentation for Python sphinxcontrib-svg2pdfconverter module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib-svg2pdfconverter
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib-svg2pdfconverter module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib-svg2pdfconverter.

%prep
%setup -q -n sphinxcontrib_svg2pdfconverter-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib/__init__.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/sphinxcontrib/__pycache__/__init__.*.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/sphinxcontrib/cairosvgconverter.py
%{py3_sitescriptdir}/sphinxcontrib/inkscapeconverter.py
%{py3_sitescriptdir}/sphinxcontrib/rsvgconverter.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/cairosvgconverter.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/inkscapeconverter.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/rsvgconverter.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_svg2pdfconverter-%{version}-py*.egg-info
