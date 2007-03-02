%define		module	modplug
#
Summary:	Python bindings for libmodplug library
Summary(pl.UTF-8):    Wiązania języka Python dla biblioteki libmodplug
Name:		python-modplug
Version:	1.0
Release:	1
License:	GPLv2
Group:		Development/Languages/Python
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:  a937f97d63fe1dadbe7ca69ae37d77ae
URL:		http://www.sacredchao.net/~piman/
BuildRequires:  python-devel
BuildRequires:  rpm-pythonprov
BuildRequires:  libmodplug-devel >= 0.7
BuildRequires:  pkgconfig >= 0.21-2
%pyrequires_eq  python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libmodplug >= 0.7

%description
This Python module lets you load and decode files supported by the ModPlug
library (which includes MODs, ITs, XMs, and so on). Its API has been chosen
to mostly match pyvorbis and pymad.

Currently it always outputs in 44100kHz stereo, 16 bits per channel. Noise
reduction, oversampling, and the highest-quality resampling filter are
enabled.

%description -l pl.UTF-8
Ten moduł języka Python pozwala na ładowanie i dekodowanie plików wspieranych
przez bibliotekę ModPlug (czyli MOD, IT, XM itd.). Jego API zostało stworzone
tak, aby jak najbardziej było zbliżone do pyvorbis i pymad.

Obecnie moduł ten dekoduje do 44100kHz stereo, 16 bitów na kanał. Zawiera także
redukcję szumów, oversampling i najwyższej jakości filtr resamplujący.

%prep
%setup -q -n %{module}-%{version}

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python ./setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
install playmod.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{py_sitedir}/*.so
%{_examplesdir}/%{name}-%{version}/
