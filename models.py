#
# script for various ORM models for project
#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://surjitkaur:surjitkaur123@localhost/sargondb'
db = SQLAlchemy(app)

#################################################
#              model for Skill                  #
#################################################
class Skill(db.Model):

    __tabelname__ = 'skill'

    skillID = db.Column(db.BigInteger, primary_key=True)
    skillName = db.Column(db.String(60))
    skillLink = db.Column(db.String(60))

    def __init__(self, skillID, skillName, skillLink):
        self.skillID = skillID
        self.skillName = skillName
        self.skillLink = skillLink

#################################################
#           model for SkillMatches              #
#################################################
class SkillMatches(db.Model):

    __tabelname__ = 'skillmatches'

    skillMatchID = db.Column(db.BigInteger, primary_key=True)
    #jobID = db.Column(db.BigInteger, ForeignKey('jobs.jobsID'))
    skillID = db.Column(db.BigInteger, ForeignKey('skill.skillID'))

    def __init__(self, skillMatchID, jobID, skillID):
        self.skillMatchID = skillMatchID
        self.jobID = jobID
        self.skillID = skillID

#################################################
#        model for companyculture               #
#################################################
class companyculture(db.Model):

    __tabelname__ = 'companyculture'

    companycultureID = db.Column(db.BigInteger, primary_key=True)
    companyculture = db.Column(db.String(90))

    def __init__(self, companycultureID, companyculture):
        self.companycultureID = companycultureID
        self.companyculture = companyculture

#################################################
#            model for CompanyType              #
#################################################
class CompanyType(db.Model):

    __tabelname__ = 'companytype'

    companyTypeID = db.Column(db.BigInteger, primary_key=True)
    companyType = db.Column(db.String(60))

    def __init__(self, companyTypeID, companyType):
        self.companyTypeID = companyTypeID
        self.companyType = companyType

#################################################
#        model for ExperienceLevel              #
#################################################
class ExperienceLevel(db.Model):

    __tabelname__ = 'experiencelevel'

    experienceLevelID = db.Column(db.BigInteger, primary_key=True)
    levelDescription = db.Column(db.String(90))
    level = db.Column(db.String(90))

    def __init__(self, experienceLevelID, levelDescription, level):
        self.experienceLevelID = experienceLevelID
        self.levelDescription = levelDescription
        self.level = level
 
#################################################
#       model for CompanyTypeMatches            #
#################################################
class CompanyTypeMatches(db.Model):

    __tabelname__ = 'companytypematches'

    companyTypeMatchID = db.Column(db.BigInteger, primary_key=True)
    companyType = db.Column(db.String(60))
    candidateID = db.Column(db.BigInteger,
                            ForeignKey('candidates.candidatesID'))

    def __init__(self, companyTypeMatchID, companyType, candidateID):
        self.companyTypeMatchID = companyTypeMatchID
        self.companyType = companyType
        self.candidateID = candidateID
 
#################################################
#            model for Candidates               #
#################################################
class Candidates(db.Model):

    __tabelname__ = 'candidates'

    candidatesID = db.Column(db.BigInteger, primary_key=True)
    reference = db.Column(db.String(90))
    nearestCity = db.Column(db.String(90))
    salary = db.Column(db.Integer)
    vaildThrough = db.Column(db.String(90))
    mobileTelephone = db.Column(db.Integer)
    email = db.Column(db.String(90))
    firstName = db.Column(db.String(90))
    lastName = db.Column(db.String(90))
    preferredJobTitle = db.Column(db.String(90))
    experienceLevelID = db.Column(db.BigInteger,
                                  ForeignKey('experience_level.experienceLevelID'))
    availableFrom = db.Column(db.String(90))
    opportunityID = db.Column(db.Integer)
    available = db.Column(db.String(90))
    location = db.Column(db.String(90))
    rate = db.Column(db.Integer)

    def __init__(self, candidatesID, reference, nearestCity, salary,
                 vaildThrough, mobileTelephone, email, firstName, lastName,
                 preferredJobTitle, ExperienceLevelID, availableFrom,
                 opportunityID, available, location, rate):
        self.candidatesID = candidatesID
        self.reference = reference
        self.nearestCity = nearestCity
        self.salary = salary
        self.vaildThrough = vaildThrough
        self.mobileTelephone = mobileTelephone
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.preferredJobTitle = preferredJobTitle
        self.ExperienceLevelID = ExperienceLevelID
        self.availableFrom = availableFrom
        self.opportunityID = opportunityID
        self.available = available
        self.location = location
        self.rate = rate

#################################################
#              model for JobMatches             #
#################################################
class JobMatches(db.Model):

    __tabelname = 'jobmatch'

    jobMatchID = db.Column(db.BigInteger, primary_key=True)
    candidatesID = db.Column(db.BigInteger,
                             ForeignKey('candidates.candidatesID'))
    jobID = db.Column(db.BigInteger, ForeignKey('jobs.jobsID'))
    interested = db.Column(db.Integer)

    def __init__(self, jobMatchID, candidatesID, jobID, interested):
        self.jobMatchID = jobMatchID
        self.candidatesID = candidatesID
        self.jobID = jobID
        self.interested = interested

#################################################
#              model for Jobs                   #
#################################################
class Jobs(db.Model):

    __tabelname__ = 'jobs'

    jobsID = db.Column(db.BigInteger, primary_key=True)
    reference = db.Column(db.String(90))
    postCategoryID = db.Column(db.BigInteger,
                               ForeignKey('category_match.categorymatchID'))
    locationCity = db.Column(db.String(90))
    salary = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    companyTypeID = db.Column(db.BigInteger,
                              ForeignKey('company_type.companyTypeID'))
    companyCultureID = db.Column(db.Integer)
    ExperienceLevelID = db.Column(db.BigInteger,
                                  ForeignKey('experience_level.'
                                             'experienceLevelID'))
    jobTitle = db.Column(db.String(90))
    jobType = db.Column(db.String(90))
    currency = db.Column(db.Integer)
    jobBenefits = db.Column(db.String(90))
    jobDescription = db.Column(db.String(90))
    educationalRequiments = db.Column(db.String(90))
    postcode = db.Column(db.Integer)
    responsibilities = db.Column(db.String(90))
    workHours = db.Column(db.String(90))
    validThough = db.Column(db.String(90))
    contractDuration = db .Column(db.String(90))

    def __init__(self, jobsID, reference, postCategoryID, locationCity, salary,
                 rate, companyTypeID, companyCultureID, ExperienceLevelID,
                 jobTitle, jobType, currency, jobBenefits, jobDescription,
                 educationalRequiments, postcode, responsibilities, workHours,
                 validThough, contractDuration):
        self.jobsID = jobsID
        self.reference = reference
        self.postCategoryID = postCategoryID
        self.locationCity = locationCity
        self.salary = salary
        self.rate = rate
        self.companyTypeID = companyTypeID
        self.companyCultureID = companyCultureID
        self.ExperienceLevelID = ExperienceLevelID
        self.jobTitle = jobTitle
        self.jobType = jobType
        self.currency = currency
        self.jobBenefits = jobBenefits
        self.jobDescription = jobDescription
        self.educationalRequiments = educationalRequiments
        self.postcode = postcode
        self.responsibilities = responsibilities
        self.workHours = workHours
        self.validThough = validThough
        self.contractDuration = contractDuration

#################################################
#          model for CategoryMatch              #
#################################################
class CategoryMatch(db.Model):

    __tabelname__ = 'categorymatch'

    categorymatchID = db.Column(db.BigInteger, primary_key=True)
    jobID = db.Column(db.Integer)
    categoryID = db.Column(db.BigInteger, db.ForeignKey('category.categoryID'),
                                                        primary_key=True)

    def __init__(self, categorymatchID, jobID, categoryID):
        self.categorymatchID = categorymatchID
        self.jobID = jobID
        self.categoryID = categoryID

#################################################
#            model for Category                 #
#################################################
class Category(db.Model):

    __tablename__ = 'category'

    categoryID = db.Column(db.BigInteger, primary_key=True)
    categoryName = db.Column(db.String(60))
    categorymatchID = db.Column(db.BigInteger,
                                db.ForeignKey('category_match.categorymatchID'))

    def __init__(self, categoryID, categoryName, categorymatchID):
        self.categoryID = categoryID
        self.categoryName = categoryName
        self.categorymatchID = categorymatchID

#################################################
#        model for CandidateNetwork             #
#################################################
class CandidateNetwork(db.Model):

    __tabelname__ = 'candidatenetwork'

    candidateNetworkID = db.Column(db.BigInteger, primary_key=True)
    candidatesID = db.Column(db.BigInteger,
                             ForeignKey('candidates.candidatesID'))
    linkedID = db.Column(db.Integer)
    website = db.Column(db.String(90))
    stackOverflow = db.Column(db.String(90))
    gitHub = db.Column(db.String(90))
    bitBucket = db.Column(db.String(90))
    twitter = db.Column(db.String(90))
    facebook = db.Column(db.String(90))

    def __init__(self, candidateNetworkID, candidatesID, linkedID, website,
                 stackOverflow, gitHub, bitBucket, twitter, facebook):
        self.candidateNetworkID = candidateNetworkID
        self.candidatesID = candidatesID
        self.linkedID = linkedID
        self.website = website
        self.stackOverflow = stackOverflow
        self.gitHub = gitHub
        self.bitBucket = bitBucket
        self.twitter = twitter
        self.facebook = facebook

if __name__ == '__main__':
    try:
        db.create_all()
        print "===================== [db created] ====================="
    except:
        #pass
        print "===================== [db not created] =====================" 