class Menu
  include Mongoid::Document
  field :name, type: String
  embedded_in :schedule
  embeds_many :dishes
end
