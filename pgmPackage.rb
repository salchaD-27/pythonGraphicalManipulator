class Pgmpackage < Formula
    include Language::Python::Virtualenv
  
    desc "A python library for graphical image manipulation"
    homepage "https://pypi.org/project/pythonGraphicalManipulator/"
    version "0.1.0" 
    url "https://github.com/salchaD-27/pythonGraphicalManipulator/archive/refs/heads/main.tar.gz"
    sha256 "9a54e1c6939fd2e91f9b8509cee03d1b840a129fc31ec9246b1a857ee13dbf34"
    license "MIT"

    def install
      system "pip3", "install", "."
    end
  end