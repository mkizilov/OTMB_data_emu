# OTMB_data_emu

## How to use
### Set up
```Shell
scram p -n NameOfYourDirectory CMSSW_13_0_3
cd NameOfYourDirectory/src/
cmsenv
git cms-init
git clone https://github.com/mkizilov/OTMB_data_emu.git -b CMSSW_13_0_3
scram b -j 8
```

### Unpack data
```shell
cmsRun IORawData/CSCCommissioning/test/readFile_b904_Run3.py firstRun=341761 inputFiles="YOURFILE.raw" maxEvents=10000 inputFilesGEM=file:runFakeGEM.raw readGEMData=True useB904ME11=True
```
### Edit emulator alignment corrections (eightstrips level)
Add desired alignment and run file. Or edit them manually here `src/L1Trigger/CSCTriggerPrimitives/data/GEMCSC/AlignmentCorrection`
```shell
python3 tools_L1Trigger/lookup_table.py
```

### Run emulator
```shell
cmsRun L1Trigger/CSCTriggerPrimitives/test/runCSCTriggerPrimitiveProducer_cfg.py run3=True unpack=True l1=True l1GEM=True unpackGEM=True dqm=True dqmGEM=True useB904ME11=True runCCLUTOTMB=True runME11ILT=True useB904ME11PositiveEndcap=True useB904GE11Long=True preTriggerAnalysis=True maxEvents=-1 inputFiles="file:YOURFILE"
```
If you want to use OTMB_data_emu_analyzer for making plots write stdout and stderr into .txt file while running emulator. You can use this command instead:
```shell
cmsRun L1Trigger/CSCTriggerPrimitives/test/runCSCTriggerPrimitiveProducer_cfg.py run3=True unpack=True l1=True l1GEM=True unpackGEM=True dqm=True dqmGEM=True useB904ME11=True runCCLUTOTMB=True runME11ILT=True useB904ME11PositiveEndcap=True useB904GE11Long=True preTriggerAnalysis=True maxEvents=-1 inputFiles="file:YOURFILE" > test.txt 2>&1
```
This will create `step_DQM.root` and `lcts2.root`
Then use https://github.com/mkizilov/OTMB_data_emu_analyzer to parse and plot this file.
### Run DQM Client
It takes `step_DQM.root` and creates `DQM_V0001_R000341761__Global__CMSSW_X_Y_Z__RECO.root`
```shell
cmsRun L1Trigger/CSCTriggerPrimitives/test/runCSCL1TDQMClient_cfg.py mc=False run3=True useB904ME11=True useGEMs=True
```
### Create plots from output root file
It takes `DQM_V0001_R000341761__Global__CMSSW_X_Y_Z__RECO.root` and creates `CSC_dataVsEmul_B904_Cosmic_Run_YOUR_TEXT_LABEL.ps`
```shell
cmsRun L1Trigger/CSCTriggerPrimitives/test/runCSCTriggerPrimitiveAnalyzer_cfg.py dataVsEmulation=True dataVsEmulationFile=file:DQM_V0001_R000341761__Global__CMSSW_X_Y_Z__RECO.root runNumber=341761 useB904ME11=True B904RunNumber=YOUR_TEXT_LABEL
```

### Convert to pdf
```shell
ps2pdf CSC_dataVsEmul_B904_Cosmic_Run_YOUR_TEXT_LABEL.ps
```

### To visualize particular events use Tao's Event Display
https://github.com/tahuang1991/gifDisplay

