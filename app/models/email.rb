class Email
  include Mongoid::Document
  field :email, type: String
  field :name, type: String
  field :status, type: String
end
