Summary:	Turboprint printers menager
Summary(pl):	Zarz±dca drukarek Turboprint
Name:		turboprint
Version:	1.62
Release:	1
License:	Commercial, not distributable
Group:		Applications/Printing
Source0:	http://www.turboprint.de/%name-%version.tgz
Source1:	%{name}.desktop
URL:		http://www.turboprint.de
BuildRequires:	cups
BuildRequires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
TurboPrint is a high-quality printer driver system for Linux built on
existing standards (lpr or CUPS printer spooler, ghostscript
interpreter for Postscript) thus achieving easy integration and
maximum compatibility with existing applications.

%description -l pl
TurboPrint jest wysokiej jako¶ci systemem sterowników dla Linuxa,
opartym na istniej±cych standardach (lpr albo kolejkowanie przez
CUPS, ghostscript dla Postscriptu). Jest wysoce integrowalny z tymi
¶rodowiskami.

%prep
%setup -q

%build
./setup

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Aplications/Printing

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Aplications/Printing/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(644,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/colors
%dir %{_datadir}/%{name}/doc
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/lib
%{_applnkdir}/Aplications/Printing/%{name}.desktop
