%global gem_name activesupport
    
%global gem_dir /usr/lib/ruby/gems/%(%ruby_rubyconf RUBY_LIB_VERSION)
%global gem_instdir %gem_dir/gems
%global gem_docdir %gem_dir/doc
%global gem_cache %gem_dir/cache

Name: activesupport-gems
Version: 5.1.4
Release: alt1.1
Summary: ActiveSupport 
Group: Development/Ruby
License: MIT,Apache2.0
Url: http://rubygems.org
packager: Denis Medvedev <nbr@altlinux.org>

Source: %name-%version.tar
BuildRequires: ruby  ruby-tools libruby-devel 
BuildArch: noarch
Obsoletes: activesupport <= 3.0

%description
ActiveSupport ruby gem


%package doc
Summary: Documentation for %name
Group: Documentation
# SyntaxHighlighter is dual licensed under the MIT and GPL licenses
License: MIT and (MIT or GPL+)
BuildArch: noarch

%description doc
Documentation for %name.

%prep
%setup -c -T
tar xvf %SOURCE0
%build
%install
cd %name-%version
#gem install --user builder*.gem
#gem install --user rack*.gem
#gem install --user erubis*.gem
#gem install --user nokogiri*.gem
#gem install --user loo*.gem
#gem install --user thor*.gem
#gem install --user mini_portile*.gem

#gem install --user action*.gem
gem install --user  --local i18n*.gem
gem install --user   --local thread*.gem
gem install --user   --local tzinfo*.gem
gem install --user --local concurrent*.gem
gem install --user --local active*.gem
#gem install --user --local rails-dom-testing*.gem
#gem install --user rails-html*.gem
#gem install --user railties*.gem
#gem install --user sprockets-3*.gem
#gem install --user *.gem
cd ~/.gem/ruby/%(%ruby_rubyconf RUBY_LIB_VERSION)
tar czvf ~/ar.tgz *

mkdir -p %buildroot/%gem_dir 
cd %buildroot/%gem_dir 
%add_findreq_skiplist /usr/lib/ruby/gems/*

tar xzvf ~/ar.tgz
rm -f gems/thread_safe-0.3.6/examples/bench_cache.rb
# this file has bad shebang 
%files
%gem_dir/*
%exclude %gem_cache
%exclude %gem_docdir


%files doc
%doc %gem_docdir

%changelog
* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.4-alt1.1
- Rebuild with Ruby 2.5.0

* Fri Dec 29 2017 Denis Medvedev <nbr@altlinux.org> 5.1.4-alt1
- freshen included gem versions

* Sun Nov 12 2017 Denis Medvedev <nbr@altlinux.org> 5.0.2-alt3
- Added obsoletes for old activesupport

* Thu Sep 14 2017 Denis Medvedev <nbr@altlinux.org> 5.0.2-alt2
- Switched to macro for gem path.

* Sun Mar 19 2017 Denis Medvedev <nbr@altlinux.org> 5.0.2-alt1
- initial build for ALT Linux Sisyphus. Based on gems.
