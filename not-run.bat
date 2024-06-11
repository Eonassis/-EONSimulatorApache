@echo off
echo Rodando eon_simulator_salvador_V12...
cd eon_simulator_salvador_V12
python31 run.py
cd ..
echo Rodando eon_simulator-Salvador-CostI-V12...
cd eon_simulator-Salvador-CostI-V12
python31 run.py
cd ..
echo Rodando eon_simulator-Salvador-P-KSP-V12...
cd eon_simulator-Salvador-P-KSP-V12
python31 run.py
cd ..
echo Rodando eon_simulator-Salvador-TSSCF-V12...
cd eon_simulator-Salvador-TSSCF-V12
python31 run.py
cd ..
echo Gerando Graficos...
python31 graficos.py
echo Graficos Gerados.
echo Processo Finalizado!
pause()

