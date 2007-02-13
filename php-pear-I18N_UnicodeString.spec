%include	/usr/lib/rpm/macros.php
%define		_class		I18N
%define		_subclass	UnicodeString
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides a way to work with self contained multibyte strings
Summary(pl.UTF-8):	%{_pearname} - sposób pracy z samodzielnymi łańcuchami znaków wielobajtowych
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	47a200e64e63dea632969015d512c0b6
URL:		http://pear.php.net/package/I18N_UnicodeString/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a method of storing and manipulating multibyte strings in PHP
without using ext/mbstring. Also allows conversion between various
methods of storing Unicode in 1-byte strings like UTF-8 and HTML
entities.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa dostarcza metodę zapisu i obróbki łańcuchów znaków
wielobajtowych w PHP bez używania rozszerzenia mbstring. Umożliwia
także konwersję między różnymi metodami zapisu Unikodu w łańcuchach
znaków jednobajtowych, takich jak UTF-8 czy encje HTML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
