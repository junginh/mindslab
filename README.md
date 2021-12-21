# mindslab

### divide_image.py
1. terminal user input 구현
2. M, N 구현
3. 나눠지지 않는경우 구현 
4. mirror, flip, 90 deg rotation 구현
5. output image 저장 구현

### merge_image.py
1. terminal user input 구현
2. 모든 경우의 수 = (N * M)!
3. output image 기준을 첫번째 리스트 이미지의 transformation 로 정함
4. openCV image stiching 고려
5. edge vector cosine similarity 시도 (inspired by: [this link](https://www.abtosoftware.com/blog/computer-vision-powers-automatic-jigsaw-puzzle-solver) Module VI. Colour Descriptor)
   - 가장 최소 거리더라도 안 맞는 경우가 생김
6. jigsaw 시도 [this keras model structure](https://gist.github.com/shivaverma/f8f51b2309fc7c9ad0a404a0ff3a2603)
   - python3 -m pip install tensorflow-macos
   - --> ERROR: Could not build wheels for h5py, which is required to install pyproject.toml-based projects
   - Jigsaw puzzle
   - JigsawGAN
   - Facebook VISSL jigsaw
   - https://avkashchauhan.medium.com/solving-block-image-puzzle-with-neural-networks-webapp-solution-5ade03e5bc8
