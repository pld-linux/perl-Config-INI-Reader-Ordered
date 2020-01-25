#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Config
%define		pnam	INI-Reader-Ordered
Summary:	Config::INI::Reader::Ordered -- .ini-file parser that returns sections in order
Name:		perl-Config-INI-Reader-Ordered
Version:	0.020
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d93fc080b21f57c1ec00f6bc428dff0b
URL:		https://metacpan.org/pod/Config::INI::Reader::Ordered
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Config::INI::Reader)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::INI::Reader::Ordered is a subclass of Config::INI::Reader
which preserves section order.  See Config::INI::Reader for all
documentation; the only difference is as presented in the /SYNOPSIS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Config/INI/Reader
%{perl_vendorlib}/Config/INI/Reader/Ordered.pm
%{_mandir}/man3/*
