Summary:	Sphinx SVG to PDF or PNG converter extension
Summary(pl.UTF-8):	Rozszerzenie Sphinksa konwertujące SVG do PDF lub PNG
Name:		python3-sphinxcontrib-svg2pdfconverter
Version:	2.1.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-svg2pdfconverter/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-svg2pdfconverter/sphinxcontrib_svg2pdfconverter-%{version}.tar.gz
# Source0-md5:	24f17b4e328b792d24d0be6b9e5617e6
URL:		https://pypi.org/project/sphinxcontrib-svg2pdfconverter/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:61.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension converts SVG images to PDF or PNG in case the builder
does not support SVG images natively (e.g. LaTeX).

%description -l pl.UTF-8
To rozszerzenie konwertuje obrazy SVG do PDF lub PNG w przypadkach, kiedy
builder sam nie obsługuje obrazów SVG (np. LaTeX).

%prep
%setup -q -n sphinxcontrib_svg2pdfconverter-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%{py3_sitescriptdir}/sphinxcontrib/cairosvgconverter
%{py3_sitescriptdir}/sphinxcontrib/inkscapeconverter
%{py3_sitescriptdir}/sphinxcontrib/rsvgconverter
%{py3_sitescriptdir}/sphinxcontrib_svg2pdfconverter-%{version}-py*.egg-info
