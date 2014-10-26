require 'sikulix'
include Sikulix

def click_if(pattern)
  click e if e = exists(pattern, 0)
  !!e
end
    
