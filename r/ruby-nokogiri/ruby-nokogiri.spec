%define Name Nokogiri
%define bname nokogiri
Name: ruby-%bname
Version: 1.5.9
Release: alt1
Summary: Ruby libraries for %Name (HTML, XML, SAX, and Reader parser)
Group: Development/Ruby
License: MIT/Ruby
URL: http://%bname.org
Source: %bname-%version.tar
Patch: %bname-%version-%release.patch

BuildPreReq: rpm-build-ruby
BuildRequires: ruby ruby-stdlibs libruby-devel ruby-racc ruby-tool-setup %_bindir/rexical
BuildRequires: libxml2-devel libxslt-devel java-devel
#BuildRequires: db2latex-xsl xhtml1-dtds

%description
%Name parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package -n %bname
Summary: HTML, XML, SAX, and Reader parser
Group: Development/Other
BuildArch: noarch
Requires: ruby >= 1.8
Requires: %name = %version-%release

%description -n %bname
%Name parses and searches XML/HTML very quickly, and also has correctly
implemented CSS3 selector support as well as XPath support.
This package contanis Ruby libraries for Nokogiri.


%package doc
Summary: Documentation for %Name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for %Name.


%prep
%setup -q -n %bname-%version
%patch -p1

DisableTest()
{
	local f="$1"

	shift
	while [ -n "$1" ]; do
		sed -i -r \
			-e "/^[[:blank:]]*def[[:blank:]]+test_$1[[:blank:]]*$/iif false" \
			-e "/^[[:blank:]]*def[[:blank:]]+test_$1[[:blank:]]*$/,/^[[:blank:]]*$/s/^[[:blank:]]*$/end\n&/" \
			"test/$f.rb"
		shift
	done
}

DisableTest test_convert_xpath multiple_filters
DisableTest html/test_node css_path_round_trip path_round_trip

%update_setup_rb


%build
%ruby_config
%ruby_build

# XXX@stanv: next lines are taken from Rakefile:
racc -l -o lib/%bname/css/generated_parser.rb lib/%bname/css/parser.y
rexical --independent -o lib/%bname/css/generated_tokenizer.rb lib/%bname/css/tokenizer.rex


%install
%ruby_install
%rdoc lib/
ls -d %buildroot%ruby_ri_sitedir/* | grep -v '/%Name$' | xargs rm -rf


%check
%ruby_vendor -I. -Ilib:ext:test setup.rb test


%files
%ruby_sitelibdir/%bname
%ruby_sitelibdir/xsd
%ruby_sitelibdir/*.jar
%ruby_sitelibdir/*.rb
%ruby_sitearchdir/*


%files -n %bname
%_bindir/*


%files doc
%ruby_ri_sitedir/*


%changelog
* Fri Apr 12 2013 Led <led@altlinux.ru> 1.5.9-alt1
- 1.5.9
- updated URL
- updated BuildRequires
- fixed Group for %%name-doc subpackage
- moved %%_bindir/nokogiri to separate subpackage

* Sat Dec 15 2012 Led <led@altlinux.ru> 1.5.5-alt2
- fixed for renamed %_bindir/rex -> %_bindir/rexical
- %%files: fixed "File listed twice"

* Fri Dec 07 2012 Led <led@altlinux.ru> 1.5.5-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Wed Mar 24 2012 Andriy Stepanov <stanv@altlinux.ru> 1.5.5-alt1
- New version

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt2
- Fix build

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.4.4.2-alt1
- [1.4.4.2]

* Wed Mar 17 2010 Timur Batyrshin <erthad@altlinux.org> 1.4.0-alt1
- [1.4.0]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.2-alt1
- [1.3.2]

* Thu Sep 25 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt1
- Initial build for ALT Linux.

