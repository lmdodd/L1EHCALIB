import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(45.01),
        MinPt = cms.double(44.99),
        PartID = cms.vint32(211),
        MaxEta = cms.double(3),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-3),
        MinPhi = cms.double(-3.14159265359) ## in radians

    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single pi pt 45'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
