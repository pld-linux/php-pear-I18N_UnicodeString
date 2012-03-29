%define		status		beta
%define		pearname	I18N_UnicodeString
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - provides a way to work with self contained multibyte strings
Summary(pl.UTF-8):	%{pearname} - sposób pracy z samodzielnymi łańcuchami znaków wielobajtowych
Name:		php-pear-%{pearname}
Version:	0.3.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	615e3f3cd9d545b16014fb69eb23dc35
Patch0:		bug-19358.patch
URL:		http://pear.php.net/package/I18N_UnicodeString/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear >= 4:1.0-22
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a method of storing and manipulating multibyte strings in PHP
without using ext/mbstring. Also allows conversion between various
methods of storing Unicode in 1-byte strings like UTF-8 and HTML
entities.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa dostarcza metodę zapisu i obróbki łańcuchów znaków
wielobajtowych w PHP bez używania rozszerzenia mbstring. Umożliwia
także konwersję między różnymi metodami zapisu Unikodu w łańcuchach
znaków jednobajtowych, takich jak UTF-8 czy encje HTML.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1

mv .%{php_pear_dir}/data/I18N_UnicodeString/README .
mv docs/%{pearname}/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/I18N/UnicodeString.php
%dir %{php_pear_dir}/I18N/Unicode
%{php_pear_dir}/I18N/Unicode/Exception.php
%{_examplesdir}/%{name}-%{version}
