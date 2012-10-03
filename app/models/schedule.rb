class Schedule
  include Mongoid::Document
  field :type, type: Integer
  field :day_of_week, type: Integer
  field :date, type: Date
  embeds_one :menu
end
