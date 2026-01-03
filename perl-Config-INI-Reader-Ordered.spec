#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Config
%define		pnam	INI-Reader-Ordered
Summary:	Config::INI::Reader::Ordered - .ini-file parser that returns sections in order
Summary(pl.UTF-8):	Config::INI::Reader::Ordered - parser plików .ini zwracający sekcje w kolejności
Name:		perl-Config-INI-Reader-Ordered
Version:	0.022
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d0f595f053ee1ab7474ca1f429f966df
URL:		https://metacpan.org/dist/Config-INI-Reader-Ordered
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Config-INI
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::INI::Reader::Ordered is a subclass of Config::INI::Reader
which preserves section order.

%description -l pl.UTF-8
Config::INI::Reader::Ordered to podklasa Config::INI::Reader,
zachowująca kolejność sekcji.

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
%{_mandir}/man3/Config::INI::Reader::Ordered.3pm*
